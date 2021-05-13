def main():
	s = input()
	t = input()

	s_ascend = "".join(sorted(s))
	t_descend = "".join(sorted(t, reverse = True))

	if s_ascend < t_descend:
		print("Yes")
	else:
		print("No")



  
if __name__ == "__main__":
  	main()