(wake_h, wake_m, sleep_h, sleep_m, k) = list(map(int, input().split()))

wake_m_all = wake_h * 60 + wake_m
sleep_m_all = sleep_h * 60 + sleep_m
sleep_m_all -= k
print(sleep_m_all - wake_m_all)