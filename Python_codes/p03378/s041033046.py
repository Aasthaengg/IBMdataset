def count_fee_station(a, n_list):
    cost = 0
    for i in n_list:
        if i in a:
            cost += 1
    return cost


def main():
    n , m , x  = map(int,input().split())
    a = list(map(int, input().split()))
    if n in a:
        a.remove(n)
    n_list_a = list(range(0,x+1))
    n_list_b = list(range(x,n+1))
    cost_a = count_fee_station(a,n_list_a)
    cost_b = count_fee_station(a,n_list_b)
    print(min(cost_a,cost_b))

if __name__ == '__main__':
    main()
