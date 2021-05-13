n = int(input())
ans = 0
tail_a_cnt = 0
top_b_cnt = 0
top_b_tail_a = 0
for i in range(n):
    s = list(input())
    top_b = False
    tail_a = False
    
    for c in range(len(s)):
        if c == 0:
            if s[c] == 'B':
                top_b = True
        else:
            if s[c] == 'B' and s[c-1] == 'A':
                ans += 1
        
        if c == len(s)-1 and s[c]=='A':
            tail_a = True
            
    top_b_cnt += top_b
    tail_a_cnt += tail_a
    top_b_tail_a += top_b*tail_a
     
ans += min(top_b_cnt, tail_a_cnt)
if top_b_cnt == tail_a_cnt == top_b_tail_a and top_b_cnt>0:
    ans -= 1
    
print(ans)