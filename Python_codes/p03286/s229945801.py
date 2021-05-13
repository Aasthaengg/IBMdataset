# ABC105C

n = int(input())
def sub(n):
    if n==0:
        return []
    k = 1
    count = 0
    pos = 1
    neg = 0
    while True:
        if (n>0 and pos>=n) or (n<0 and abs(neg)>=abs(n)):
            break
        count += 1
        k *= (-2)
        if k>0:
            pos += k
        else:
            neg += k
#     print(n, pos, neg, k)
    return [count] + (sub(n-k) if n>0 else sub(n-k))
out = sub(n)
if not out:
    print(0)
else:
    s = ["0"] * (max(out)+1)
    for item in out:
        s[item] = "1"
    print("".join(s[::-1]))