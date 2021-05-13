#-*-coding:utf-8-*-

def main():
    numbers=[]
    n = int(input())
    numbers=list(map(int,input().split()))
    sort_numbers=sorted(numbers)
# left/right算出はsorted arrayで
    left=sort_numbers[n//2-1]
    right=sort_numbers[n//2]
# loopは元の配列で
    for i in numbers:
        if i > left:
            print(left)
        else:
            print(right)

if __name__=="__main__":
    main()