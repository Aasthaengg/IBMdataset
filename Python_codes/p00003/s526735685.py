#-*-coding:utf-8-*-

def get_input():
    for i in range(int(input())):
        yield "".join(input())

if __name__ == "__main__":
    array = list(get_input())
    
    for i in range(len(array)):        
        a,b,c = array[i].split()
        if int(a)**2 + int(b)**2 == int(c)**2:
            print(u"YES")
        elif int(c)**2 + int(a)**2 == int(b)**2:
            print(u"YES")
        elif int(b)**2 + int(c)**2 == int(a)**2:
            print(u"YES")
        else:
            print(u"NO")