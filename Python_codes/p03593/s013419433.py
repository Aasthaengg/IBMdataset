from collections import Counter
H,W=map(int,input().split())
a=[list(input()) for _ in range(H)]

tmp=[]
for j in a:
  for k in j:
    tmp.append(k)
d=dict(Counter(tmp))
#print(d)

odd=0
even_4=0
even_2=0
even_4_sum=0
odd_list=[]

for char in d:
    if d[char]%2==1:
        odd +=1
        odd_list.append(char)
    else:
        if d[char]%2==0:
            k= d[char]//4
            even_4 += k
            even_4_sum += k*4
            even_2 += (d[char]-4*k)//2
#print(odd,even_4,even_2)


ans="Yes"
if H==1 or W==1:
    m = max(H,W)
    if m%2==1:
        if odd !=1:
            ans="No"
    else:
        if odd >= 1:
            ans="No"
    
else:
    if H%2==0 and W%2==0:
        if odd>0 or even_2>0:
            ans="No"
    elif H%2==1 and W%2==1:
        if odd !=1:
            ans="No"
        else:
            s=d[odd_list[0]]
            u = s//4
            v = (s-u)//2  # s=4*u+2*v+1
            #print("even_4_sum",even_4_sum)
            #print(H,W,(H-1)*(W-1))
                  
            if even_4_sum+4*u< (H-1)*(W-1):
                ans="No"
            #else:
            #    even_4_amari = even_4_sum- (H-1)*(W-1)
            #    must_4_maxi = 4*(min(H,W)//2)
            #    print(even_4_amari, must_4_maxi)
            #    #must_4_mini = 4*(min(H,W)//2)
            #    if even_4_amari > must_4_maxi:
            #        ans="No"
                
    else:
        if odd >=1:
            ans="No"
        else:
            gu = H if H%2==0 else W
            if 2*even_2>gu:
                ans="No"

print(ans)