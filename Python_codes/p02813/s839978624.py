import itertools

def main():
    number = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    num_list = list(range(1, number+1))
    permu = list(itertools.permutations(num_list, number))
    where_p = permu.index(p)
    where_q = permu.index(q)
    print(abs(where_p-where_q))
if __name__ == '__main__':
    main()