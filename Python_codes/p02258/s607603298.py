def getsub(arr):
    minv = arr[0]
    maxdist = arr[1] - minv

    for v in arr[1:]:
        # update maxdist
        maxdist = max(maxdist, v- minv)

        # update minv
        minv = min(minv, v)

    return maxdist

def main():
    # get input
    N = int(input())
    arr = [int(input()) for i in range(N)]

    # get sub
    print(getsub(arr))

if __name__ == '__main__':
    main()