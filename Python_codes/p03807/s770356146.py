n = int(input())
a = list(map(int,input().split()))
a_sum = sum([a[i]%2 for i in range(n)])
print("YES" if (a_sum % 2 == 0) else "NO")