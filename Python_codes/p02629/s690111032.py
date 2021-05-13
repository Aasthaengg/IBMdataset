import string

n = int(input())
num = {k:v for k,v in zip(range(26),string.ascii_lowercase)}
#num[0] = "z"

ans = ""
while True:
    n -= 1
    ans += num[n % 26]
    n //= 26
    if (n == 0): 
        print(ans[::-1])
        exit()