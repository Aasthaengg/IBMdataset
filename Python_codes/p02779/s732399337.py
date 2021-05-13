def main():
    N = int(input())
    List = list(map(int,input().split()))
    Set = set()
    for i in List:
        if i in Set:
        	print('NO')
        	return
        Set.add(i)
    print('YES')
    return
main()