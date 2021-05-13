N = int(input())

ans = 0
tail_A = 0
head_B = 0
head_B_and_tail_A = 0

for i in range(N):
    s = str(input())
    ans += s.count("AB")

    if s[0]=="B":
        if s[-1]=="A":
            head_B_and_tail_A += 1
        else:
            head_B += 1
    elif s[-1]=="A":
        tail_A += 1

if head_B_and_tail_A >= 2:
    ans += head_B_and_tail_A - 1
    head_B_and_tail_A = 1

use_head_B_and_tail_A = min(head_B_and_tail_A,tail_A,head_B)
head_B_and_tail_A -= use_head_B_and_tail_A
tail_A -= use_head_B_and_tail_A
head_B -= use_head_B_and_tail_A
ans += 2*use_head_B_and_tail_A
#この段階でどれかは使い果たしている

use_num = min(head_B_and_tail_A,tail_A)
head_B_and_tail_A -= use_num
tail_A -= use_num
ans += use_num

use_num = min(head_B_and_tail_A,head_B)
head_B_and_tail_A -= use_num
head_B -= use_num
ans += use_num

use_num = min(tail_A,head_B)
#もう残りパターンは無いので算出の必要ないので省略
ans += use_num

print(ans)