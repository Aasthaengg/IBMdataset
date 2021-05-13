n, k = map(int, input().split())
a = list(set(map(int, input().split())))
if k>max(a):
    print('IMPOSSIBLE')
    exit()

def gcd_base(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def gcd(num_list):
    ans = 0
    for i in num_list:
        ans = gcd_base(ans, i)
    return ans

if k%gcd(a)==0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')