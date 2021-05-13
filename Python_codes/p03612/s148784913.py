N = int(input())
p_list = [0] + [int(e) for e in input().split()]

ans = 0
i = 1

if p_list[1] == 1:
    ans += 1
    #print("swap",p_list[1],"⇔",p_list[2])
    p_list[1],p_list[2] = p_list[2],p_list[1]

i += 1

while i <= N-1:
    if p_list[i] == i:
        if p_list[i+1] == i+1:
            ans += 1
            #print("swap",p_list[i],"⇔",p_list[i+1])
            p_list[i],p_list[i+1] = p_list[i+1],p_list[i]
        else:
            ans += 1
            #print("swap",p_list[i],"⇔",p_list[i-1])
            p_list[i],p_list[i-1] = p_list[i-1],p_list[i]
            
    i += 1
    
if p_list[N] == N:
    ans += 1
    
#print(p_list)
print(ans)