n = int(input())
a = list(map(int,input().split()))

a.sort(reverse = True)
a_center = [a[i] for i in range(2*n) if i%2==1]

print(sum(a_center))