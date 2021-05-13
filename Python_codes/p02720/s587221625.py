import queue

def main():
    k = int(input())
    q = queue.Queue()
    for i in range(1, 10):
        q.put(str(i))
    ans = ""
    for i in range(1, k+1):
        ans = q.get()
        if i < k:
            p = int(ans[-1])
            if p == 0:
                q.put(ans + "0")
                q.put(ans + "1")
            elif p == 9:
                q.put(ans + "8")
                q.put(ans + "9")
            else:
                for v in range(p-1, p+2):
                    q.put(ans + str(v))
    print(ans)

if __name__ == "__main__":
    main()