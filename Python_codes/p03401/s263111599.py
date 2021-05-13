
def main():
    n = int(input())
    a_s = [0] + list(map(int,input().split())) + [0]
    default = sum([abs(a_s[i-1] - a_s[i]) for i in range(1,len(a_s))])
    answer = 0
    for i in range(1,len(a_s)-1):
        if (a_s[i] >=  a_s[i-1]) == (a_s[i+1] >= a_s[i]):
            #長さは変わらず
            answer = default
        else:
            answer = default - abs(a_s[i]-a_s[i-1]) - abs(a_s[i+1]-a_s[i]) + abs(a_s[i+1] - a_s[i-1])
        print(answer)





if __name__ == '__main__':
    main()
