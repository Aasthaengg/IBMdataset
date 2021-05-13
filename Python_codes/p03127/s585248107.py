N = int(input())
A_list = list(map(int, input().split()))

def gcd(v1, v2):
    if v2 == 0:
        return v1
    return gcd(v2, v1%v2)

tmp = A_list[0]
for a in A_list:
    tmp = gcd(tmp, a)

print(tmp)