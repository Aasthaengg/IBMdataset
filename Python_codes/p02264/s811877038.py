from collections import deque

def main():
    N, Q = [int(i) for i in input().split()]
    Ts = deque([])

    for _ in range(N):
        name, time = [i for i in input().split()]
        Ts.append({
            "name": name,
            "time": int(time)
        })

    cur_t = 0

    while len(Ts):
        task = Ts.popleft()

        # 終わらない
        if task["time"] > Q:
            task["time"] -= Q
            cur_t += Q
            Ts.append(task)
        else:
            cur_t += task["time"]
            print(task["name"], cur_t)


main()

