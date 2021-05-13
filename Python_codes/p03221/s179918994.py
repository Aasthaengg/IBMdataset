
url = "https://atcoder.jp//contests/abc113/tasks/abc113_c"

def main():
    t = list(map(int, input().split()))
    town = {k: [] for k in range(1, t[0]+1)}
    all_town = []
    for _ in range(t[1]):
        tmp = list(map(int, input().split()))
        all_town.append(tmp)
        town[tmp[0]].append(tmp[1])
    ans = {}
    for k in town:
        town[k].sort()
        tmp_dic = {town[k][i]: str(k).zfill(6)+str(i+1).zfill(6) for i in range(len(town[k]))}
        ans.update(tmp_dic)
    for at in all_town:
        print(ans[at[1]])


if __name__ == '__main__':
    main()
