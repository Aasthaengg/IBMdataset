#-*-coding:utf-8-*-

def digit_sum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)

def main():
    n = input()
    digit=len(n)
    nine_numbers=n.find('9')
    limit=0

    if int(n)<=9:
        print(n)

    elif digit==nine_numbers:
        print(9*int(nine_numbers))

    else:
        max_ans = digit_sum(n)
        head=int(n[0])-1
        limit=str(head)+'9'*(digit-1) 
        ans = max(max_ans,digit_sum(limit))
        print(ans)

if __name__=="__main__":
    main()