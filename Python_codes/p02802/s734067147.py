import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readlines

from collections import defaultdict

def main():

    ac_num = 0
    pt_num = 0

    C = defaultdict(lambda: {"status":False, "penaulty":0} )

    lines = input()
    N, M = list(map(int, lines[0].split()))
    for i in range(1, M+1):
        pi, si = lines[i].split()
        pi = int(pi)
        if C[pi]["status"]:
            continue
        else:
            if si == "AC":
                C[pi]["status"] = True
                ac_num += 1
            else:
                C[pi]["penaulty"] += 1

    for i in range(1, N+1):
        if C[i]["status"]:
            pt_num += C[i]["penaulty"]

    print(ac_num, pt_num)

main()