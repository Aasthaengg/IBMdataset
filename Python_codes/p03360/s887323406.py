s = list(map(int, input().split()))
k = int(input())
s.sort(reverse=True)
print(s[0]*(2**k)+s[1]+s[2])