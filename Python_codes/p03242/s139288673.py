a=list(input())
for i,j in enumerate(a):
        if j=="9":
            a[i]="1"
        else:
            a[i]="9"
print("".join(a))    

