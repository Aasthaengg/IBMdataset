h1, m1, h2, m2, k = map(int, input().split())

wake_time = h2*60 + m2 - (h1 *60 + m1);

if wake_time > k:
    print(wake_time - k);
else:
    print(0);
