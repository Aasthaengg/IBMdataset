s = input()
k = int(input())

if len(set(s)) == 1:
    print((len(s))*k//2)
    exit()

first, last = s[0], s[-1]
first_flag = 1
a, b  = 0, 0
tmp = s[0]
tmp_cnt = 0
cnt = 0

for i in range(len(s)):
    c = s[i]
    if c == first and first_flag:  # 最初に続く文字数をカウント (a)
        a += 1
    elif c != first:
        first_flag = 0
    
    if c == tmp:  # s単体のとき必要な操作回数を求める (cnt)
        tmp_cnt += 1
    else:
        cnt += (tmp_cnt // 2)
        tmp_cnt = 1
        tmp = c
        
    if i == len(s) -1:  # 最後に続く文字数を取得 (b)
        b = tmp_cnt
        cnt += (tmp_cnt // 2)

if first != last:  # sの最初の文字と最後の文字が違う場合
    ans = cnt * k
else:  # sの最初の文字と最後の文字が同じ場合
    ans = cnt * k - (a//2 + b//2 - (a+b)//2)*(k-1)

print(ans)