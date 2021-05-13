import sys

"""
H1時M1分起床
H2時M2分就寝
K分勉強
"""
 
H1, M1, H2, M2, K = map(int, sys.stdin.read().split())
 
awake_time = H1 *60 + M1
sleep_time = H2 *60 + M2
start_limit_time = sleep_time - K
can_study_time = start_limit_time - awake_time
 
print(can_study_time)
