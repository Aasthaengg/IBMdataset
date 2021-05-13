S, T = map(str, input().split())
A, H = map(int, input().split())

counter = {
    S: A,
    T: H
}

U = input()

counter[U] -= 1

print(counter[S], counter[T])
