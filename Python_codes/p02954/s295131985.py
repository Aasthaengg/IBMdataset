s=input()

children=[0]*len(s)
num_R=0
num_L=0
for i in range(len(s)-1):
    if s[i]=='R':
        num_R+=1
        if s[i+1]=='R':
            continue
        elif s[i+1]=='L':
            R_id=i
            L_id=i+1
            if num_R%2==0:
                children[R_id]+=num_R//2
                children[L_id]+=num_R//2
            else:
                children[R_id]+=num_R//2 + 1
                children[L_id]+=num_R//2
    elif s[i]=='L':
        num_L+=1
        if s[i+1]=='L':
            continue
        elif s[i+1]=='R':
            if num_L%2==0:
                children[R_id]+=num_L//2
                children[L_id]+=num_L//2
            else:
                children[R_id]+=num_L//2
                children[L_id]+=num_L//2 + 1
            num_R=0
            num_L=0

num_L+=1
if num_L%2==0:
    children[R_id]+=num_L//2
    children[L_id]+=num_L//2
else:
    children[R_id]+=num_L//2
    children[L_id]+=num_L//2 + 1

print(*children)
