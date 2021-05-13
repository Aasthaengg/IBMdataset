def counting_sort(array,city,road):
    bucket = [0] * city

    for i in range(road):
        for j in range(2):
            bucket[ (array[i][j] - 1) ] += 1

    return bucket

def main():
    n,m = map(int, input().split())
    way = [list(map(int,input().split())) for _ in range(m)]
    ans_list = counting_sort(way, n, m)
    for k in range(n):
        print( ans_list[k] )

main()