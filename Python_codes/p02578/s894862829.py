a=input()
b=input()
c=b.split()
d=map(int,c)
main=list(d)
sum=0
for i in range(len(main)-2):
    stool=main[i]-main[i+1]
    if stool>0:
        main[i+1]+=stool
        sum+=stool

stool=main[len(main)-2]-main[len(main)-1]
if stool>0:
    sum+=stool
    main[len(main)-1]+=stool

print(sum)    
