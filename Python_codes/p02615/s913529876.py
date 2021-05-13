N = int(input())
a = list(map(int,input().split()))


a_sort = sorted(a, reverse=True)

a_sum = a_sort[0]

if (N-2) % 2 == 0:
    for i in range(int((N-2)/2)):
        a_sum += 2*a_sort[i+1]
    print(a_sum)
else:
    for i in range((N-2)//2):
        a_sum += 2*a_sort[i+1]
    print(a_sum+a_sort[(N-2)//2 + 1])