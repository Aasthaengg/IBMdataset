n, k = list(map(int, input().split()))
s=input()

before = s[0:k-1]
low = s[k-1]
low = low.lower()
after = s[k:]

print(before+low+after)