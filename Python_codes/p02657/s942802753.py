def main():
    a,b = map(float,input().split())
    x = a*b
    y = x%1
    z = int(x-y)
    if x-y-z > z+1-(x-y):
        print(z+1)
        return
    else:
        print(z)
        return
main()