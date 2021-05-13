#coding: UTF-8

def Range(a,b,c):
    if a < b and b < c:
        return "Yes"
    else:
        return "No"

if __name__=="__main__":
    a = input().split(" ")
    ans = Range(int(a[0]),int(a[1]),int(a[2]))
    print(ans)