def linearSearch(key, list):
    for e in list:
        if key == e:
            return 1
    return 0


N1 = int(input())
arr1 = [int(n) for n in input().split()]
N2 = int(input())
arr2 = [int(n) for n in input().split()]

print(sum([linearSearch(key, arr1) for key in arr2]))

