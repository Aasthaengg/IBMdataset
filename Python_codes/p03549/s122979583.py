N,M = map(int, input().split())

## 正解できるやつ
_0 = (N-M)*100

## 1/2のやつ
_1 = 1900 * M

ans = (_0 + _1) * (2**M) 

print(ans)