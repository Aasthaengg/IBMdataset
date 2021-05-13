n = int(input())
mxa = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > mxa:
        mxa = a
        mxb = b
print(mxa+mxb)
