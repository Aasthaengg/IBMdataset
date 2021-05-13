def main():
    N, L = map(int, input().split())
    tastes = []
    num = []
    perfectPie = 0
    for i in range(N):
        perfectPie += i + L
        tastes.append(i + L)
        num.append(abs(i + L))
    num.sort()
    if num[0] in tastes:
        print(perfectPie - num[0])
    else:
        print(perfectPie + num[0])
main()  