#CODE FESTIVAL 2016 qual A
"""
もし一周回せるなら回してコストを払う
そうでないなら何もせずに次のアルファベットへ
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
kijun = ord("a")
alpha = [i for i in range(kijun,kijun+26)]
mod = 26

s = readline().rstrip().decode('utf-8')
k = int(readline())

ans = []
for i in s:
    if i == "a":
        ans.append(i)
    elif i == "z":
        if k >= 1:
            ans.append("a")
            k -= 1
        else:
            ans.append(i)
    else:
        if k >= kijun+26 - ord(i):
            ans.append("a")
            k -= kijun+26 - ord(i)
        else:
            ans.append(i)
if k:
    ans[-1] = chr(kijun+(ord(ans[-1])-kijun+k)%mod)
print("".join(ans))