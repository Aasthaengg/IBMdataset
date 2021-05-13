N, M = map(int, input().split())
l = sorted(list(set(map(int, input().split()))))

df = l[0]
#print("df", df)

s = len(bin(df)) - 2
#print("s", s)

count = 0
for i in range(s):
    if df % 2:
        break
    df //= 2
    count += 1
    
#print("count", count)

l = tuple(map(lambda x:x // (2**count), l))
#print("l", l)

for i in l:
    if i % 2 == 0:
        print(0)
        exit()

def gcd(a, k):
    if k:
        return gcd(k, a % k)
    return a

ans = l[0]
for i in l:
    ans = ans * i // gcd(ans, i)

print(-(-(M // (ans * 2**(count - 1))) // 2))
