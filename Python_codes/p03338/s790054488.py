N = int(input())
S = input()

result =[]

for i in range(N):
    left = []
    right= []
    for l in range(0,i):
        if S[l] not in left:
            left.append(S[l])
        else:
            continue

    
     
    for r in range(i,N):
        if S[r] not in right:
             right.append(S[r])
        else:
            continue


    count =0
    for i in left:
        for  s in right:
            if i == s :
                count +=1
    result.append(count)
    

print(max(result))
