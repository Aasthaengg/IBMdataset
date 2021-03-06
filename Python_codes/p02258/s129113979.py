#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D
#?????§??????
#??????????????????????????°???????????????????????¢?????´?????????????????????
def get_maximum_profit(value_list, n_list):
    minv = pow(10,10) + 1
    profit = -minv
    for v in value_list:
        profit = max(profit, v - minv) 
        minv = min(minv, v)
    return profit

def main():
    n_list = int(input())
    target_list = [int(input()) for i in range(n_list)]
    print(get_maximum_profit(target_list, n_list))
    
if __name__ == "__main__":
    main()