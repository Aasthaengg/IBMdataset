def main():
    h,w,a,b = map(int,input().split()) 
    x=[["0" for _ in range(w)] for _ in range(h)]
    for i in range(a):
        for j in range(b):
            x[j][i]="1"
    for i in range(w-a):
        for j in range(h-b):
            x[b+j][a+i]="1"
    for i in range(len(x)):
        print(''.join(x[i]))
if __name__ == "__main__":
    main()