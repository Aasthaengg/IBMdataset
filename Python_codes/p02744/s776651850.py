n = int(input())
res = [-1] * n
def do(a, b):
    #print("do",a,b)
    if a >= n:
        return
    res[a] = b
    if a == n - 1:
        print("".join(list(map(lambda x: chr(ord("a") - 1 + x), res))))
        return
    for i in range(1, max(res[0:a+1])+2):
        do(a + 1, i)
do(0, 1)
