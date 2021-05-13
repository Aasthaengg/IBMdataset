#AGC037-A Dividing a String
"""
分割した時に前の分割したものとかぶらないように
分割数を最大化せよ
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')

res = ""
ans = [""]
for i in s:
    if res == "":
        res += i
    else:
        res += i
    if ans[-1] != res:
        ans.append(res)
        res = ""
if res != "" and ans[-1] != res:
    ans.append(res)
print(len(ans)-1)
