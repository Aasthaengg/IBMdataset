r,d,x = map(int,input().split())
def saiki(r,x,d,number):
    number +=1
    if number <=2010:
        x = r*x-d
        print(x)
        saiki(r,x,d,number)
saiki(r,x,d,2000)