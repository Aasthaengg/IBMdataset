H,W,K=map(int,input().split())
l=[]
for i in range(H):
    S=input()
    l.append(S)
l_2d="".join(l)
x=l_2d.count("#")
for i in range(W):
    S=""
    for j in range(H):
        S+=l[j][i]
    l.append(S)
ans=0
for i in range(2**(H+W)):
    bag=[]
    h=[]
    w=[]
    for j in range(H+W):
        if ((i>>j)&1):
            bag.append(l[j])
            if j<H:
                h.append(j)
            else:
                w.append(j-H)
    bag_2d="".join(bag)
    y=bag_2d.count("#")
    for k in h:
        for m in w:
            if l[k][m]=="#":
                y-=1
    if x-y==K:
        ans+=1
print(ans)


        




    









        

    









    

        




    















    



    





    






        






    
















        


























            
    


    


    
    














    


    












