import math

def conbination(n, r): #nCrを求める
    # nCr = n! //(r! * (n-r)!)
    return math.factorial(n) //(math.factorial(r) * math.factorial(n-r))

N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse = True)
ave = (sum(v[:A]))/A
print (ave)

tmp_count = 1 #最初のA個の中にA番目と同じものが何個あるか
tmp = v[0]
for i in range(1, A):
    if v[i] == tmp:
        tmp_count += 1
    else:
        tmp = v[i]
        tmp_count = 1

total_count = tmp_count #全体でA番目と同じものが何個あるか
for i in range(A, N):
    if tmp == v[i]:
        total_count += 1
    else:
        break

ans = 0
if ave == tmp: #ここまで全て同じとき
    # print ('A')
    # for i in range(A, total_count + 1):
    for i in range(A, min(total_count + 1, B + 1)):
        ans += conbination(total_count, i)
else:
    ans += conbination(total_count, tmp_count)

print (ans)
