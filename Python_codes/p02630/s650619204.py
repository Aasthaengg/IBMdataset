n = int(input())
a_list = list(map(int, input().split()))
sum_a = sum(a_list)
num_a = [0]*(10**5)
for i in a_list:
    num_a[i-1] += 1
    
q = int(input())
for _ in range(q):
    b, c = list(map(int, input().split()))
    sum_a = sum_a + c * num_a[b-1] - b *num_a[b-1]
    num_a[c-1] += num_a[b-1]
    num_a[b-1] = 0
    print(sum_a)