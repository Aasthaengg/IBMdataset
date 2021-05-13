def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)

def main():
    while 1:
        try:
            a = list(map(int, input().split()))
            b = gcd(a[0],a[1])
            c = a[0]/b*a[1]
            #d = [b,c]
            print('%d %d' % (b,c))
        except:
            break
            
main()          

