s = input()

up = 0
down = 0
prev_x = ''
up_cnt = 0
down_cnt = 0
ans = 0

for i in range(len(s)):
    if (prev_x =='<'or prev_x ==''):
        if s[i] == '<':
            up_cnt += 1
        else: # s[i] == '>' at top
            up = up_cnt
            up_cnt = 0
            down_cnt =+1
            
    else: # prev_x = '>'
        if s[i] == '>':
            down_cnt += 1
        else: # s[i] ='<' at bottom
            down = down_cnt
            down_cnt =0
            up_cnt += 1
            if up == 0:
                ans += (down*(down+1))/2
            else:
                if up > down:
                    ans += (up*(up+1))/2 + (down*(down-1))/2
                else:
                    ans += (up*(up-1))/2 + (down*(down+1))/2
    prev_x = s[i]

if up_cnt > 0 and down_cnt == 0:
    ans += (up_cnt*(up_cnt+1))/2
elif down_cnt > 0 and up_cnt == 0:
    if up > down_cnt:
        ans += (up*(up+1))/2 + (down_cnt*(down_cnt-1))/2
    else:
        ans += (up*(up-1))/2 + (down_cnt*(down_cnt+1))/2

print(int(ans))